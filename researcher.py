import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.utilities import SerpAPIWrapper
from langchain_classic.agents import AgentExecutor, create_react_agent, Tool
# 引入 PromptTemplate 來處理手寫的範本
from langchain_core.prompts import PromptTemplate 
from serpapi import GoogleSearch

# 匯入分離後的 Prompt (包含新的 REACT_PROMPT_TEMPLATE)
from prompt import RESEARCHER_PROMPT_TEMPLATE, REACT_PROMPT_TEMPLATE

load_dotenv()

# 1. 大腦 (Groq)
llm = ChatGroq(
    temperature=0,
    model_name="llama-3.3-70b-versatile", 
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# 2. 工具 (Yahoo 搜尋)
def yahoo_search_func(query: str):
    """強行對接 Yahoo 的 p 參數"""
    search = GoogleSearch({
        "engine": "yahoo",
        "p": query,  # Yahoo 專用參數
        "api_key": os.getenv("SERPAPI_API_KEY"),
        "hl": "zh-tw"
    })
    res = search.get_dict()
    
    # 整理搜尋結果，只抓標題跟摘要
    organic_results = res.get("organic_results", [])
    if not organic_results:
        return "Yahoo 搜尋找不到相關結果。"
    
    formatted_res = []
    for r in organic_results[:5]: # 抓前 5 筆
        title = r.get("title", "無標題")
        snippet = r.get("snippet", "")
        formatted_res.append(f"標題: {title}\n摘要: {snippet}")
    
    return "\n\n".join(formatted_res)

# 定義工具給 Agent 使用
tools = [
    Tool(
        name="Yahoo_Search",
        func=yahoo_search_func,
        description="當你需要搜尋即時資訊、技術趨勢或半導體市場動態時使用。輸入關鍵字即可。"
    )
]

# 3. 建立 Agent - 使用手動定義的 Prompt
prompt = PromptTemplate.from_template(REACT_PROMPT_TEMPLATE)

agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True, 
    handle_parsing_errors=True,
    max_iterations=12,             # 增加思考次數到 12 次
    return_intermediate_steps=True, # 重要：回傳每一步的動作與觀察，讓我們能夠記錄調研過程
    early_stopping_method="generate" # 重要：次數到時，強制要求大腦根據現有資料生成最後答案
)

if __name__ == "__main__":
    user_topic = input("你想用 Yahoo 調研什麼主題？ ")
    query = RESEARCHER_PROMPT_TEMPLATE.format(user_topic=user_topic)
    
    print(f"\n🚀 正在針對「{user_topic}」進行全方位調研...\n")
    
    try:
        # 執行調研
        result = agent_executor.invoke({"input": query})
        # --- 整理要寫入 Markdown 的內容 ---
        full_report = f"# 深度調研報告：{user_topic}\n\n"
        
        # A. 加入中間的調研過程 (搜尋到的原始資料)
        full_report += "## 🔍 調研過程與原始資料\n"
        for i, (action, observation) in enumerate(result["intermediate_steps"]):
            full_report += f"### 步驟 {i+1}: 執行動作 [{action.tool}]\n"
            full_report += f"**搜尋關鍵字**: `{action.tool_input}`\n\n"
            full_report += f"**搜尋結果摘要**:\n{observation}\n\n"
            full_report += "---\n"

        # B. 加入最後的綜合分析
        full_report += "\n## 💡 綜合分析結論\n"
        full_report += result["output"]
        
        # --- 儲存檔案 ---
        filename = f"{user_topic}_完整調研報告.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(full_report)
            
        print(f"\n✅ 原始資料與結論已全部儲存至：{filename}")
            
    except Exception as e:
        print(f"\n❌ 執行時發生錯誤: {e}")