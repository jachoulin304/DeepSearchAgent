import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.utilities import SerpAPIWrapper
from prompt import TEST_SEARCH_QUERY

load_dotenv()

def test_setup():
    print("--- 正在測試全免費 API 組合 ---")
    # 1. 測試 Groq 大腦
    try:
        llm = ChatGroq(model_name="llama3-70b-8192")
        print("✅ Groq 大腦連線成功！")
    except Exception as e:
        print(f"❌ Groq 連線失敗: {e}")
    # 1. 測試 Yahoo 搜尋 (修正參數)
    try:
        # 明確指定 engine 為 yahoo
        params = {
            "engine": "yahoo",
            "p": TEST_SEARCH_QUERY, # Yahoo 的搜尋參數關鍵字是 'p' 而不是 'q'
            "hl": "zh-tw"
        }
        search = SerpAPIWrapper(params=params)
        
        # 注意：這裡直接呼叫 run()，它會使用 params 裡的 p
        res = search.run(TEST_SEARCH_QUERY)
        print(f"✅ Yahoo 搜尋成功！結果摘要：\n{res[:200]}...")
    except Exception as e:
        print(f"❌ Yahoo 搜尋失敗: {e}")

if __name__ == "__main__":
    test_setup()