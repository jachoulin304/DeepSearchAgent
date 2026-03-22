# prompts.py

# 1. 測試 Yahoo 搜尋用的關鍵字
TEST_SEARCH_QUERY = "FPGA-based LSTM accelerator HLS optimization 2026"

# 2. 專業分析師的指令範本
RESEARCHER_PROMPT_TEMPLATE = """
你是一位資深的「半導體產業戰略顧問」與「硬體架構專家」。
請針對「{user_topic}」進行深度技術與市場分析。

你的報告必須包含以下專業維度：
1. **產業鏈分工**：明確指出上游 EDA/IP、中游晶圓代工（如 TSMC 奈米製程進度）、下游封測的現況。
2. **核心技術關鍵指標**：如果是技術類，請分析其功耗（Power）、性能（Performance）、面積（Area, PPA）。
3. **數據驅動分析**：搜尋具體的市場成長率（CAGR）、產值數據或最新的技術論文結論（如 FPGA HLS 最佳化成果）。
4. **競爭格局**：不僅列出公司名，要分析其技術護城河。

請使用繁體中文，並以結構清晰的 Markdown 格式撰寫，包含「關鍵發現摘要」、「深度分析表」、「未來展望」。
"""

# 3. 手動定義 ReAct Prompt (取代原本的 hub.pull)
# 這是 Agent 思考的核心結構，不可隨意更改括號內容
REACT_PROMPT_TEMPLATE = """Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}
"""