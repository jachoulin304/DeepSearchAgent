import os
from dotenv import load_dotenv
from langchain_community.utilities import SerpAPIWrapper
from prompts import TEST_SEARCH_QUERY

load_dotenv()

def test_yahoo():
    print("--- 正在測試 Yahoo 搜尋 (SerpApi) ---")
    try:
        search = SerpAPIWrapper(params={"engine": "yahoo"})
        res = search.run(TEST_SEARCH_QUERY)
        print(f"✅ Yahoo 搜尋成功！結果摘要：\n{res[:200]}...")
    except Exception as e:
        print(f"❌ Yahoo 搜尋失敗: {e}")

if __name__ == "__main__":
    test_yahoo()