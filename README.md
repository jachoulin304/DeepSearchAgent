DeepSearchAgent 是一個基於 AI Agent 的自動化網路調研工具。它模擬了專業分析師的工作流程，能夠針對特定主題進行深度搜尋、資料整合，並自動生成結構嚴謹、內容詳盡的調研報告。

🚀 核心功能
自動化深度調研：只需輸入一個主題，Agent 會自動拆解搜尋任務、執行網頁搜尋並抓取關鍵資訊。

多層次思考架構：結合 RAG (Retrieval-Augmented Generation) 與 Agent 邏輯，不僅是搜尋，更具備分析與總結能力。

結構化報告生成：自動產出包含背景分析、技術細節、市場趨勢與結論的 Markdown 格式報告（如專案中的半導體調研範例）。

Prompt 工程優化：內建專門為調研場景設計的提示詞模板 (prompt.py)，確保輸出內容的專業度與精準度。

📂 檔案結構
researcher.py: 核心邏輯，定義了 Agent 如何執行搜尋與分析流程。

prompt.py: 存放系統指令（System Prompts），負責引導 AI 的分析行為。

check_model.py: 用於檢查與驗證模型連線狀態。

test_api.py: API 功能測試工具。

半導體_完整調研報告.md: 專案產出的實作範例，展示了系統生成的高品質報告內容。

🛠️ 技術棧
語言: Python 100%

AI 核心: 基於 LLM (如 GPT-4 或 Claude) 的 API 調用

搜尋整合: 整合網頁搜尋 API 實時抓取最新資訊
