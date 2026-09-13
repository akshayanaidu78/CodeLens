import { useEffect, useRef, useState } from "react";
import Editor from "@monaco-editor/react";
import "./App.css";

function App() {
  const [code, setCode] = useState(
`def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True`
  );

  const [selectedLine, setSelectedLine] = useState(null);
  const [explanation, setExplanation] = useState(null);

  const decorationIds = useRef([]);
  const editorRef = useRef(null);

  function handleEditorMount(editor) {
    editorRef.current = editor;

    editor.onMouseDown((event) => {
      if (!event.target.position) {
        return;
      }

      const lineNumber = event.target.position.lineNumber;

      console.log("Clicked line:", lineNumber);

      setSelectedLine(lineNumber);

      decorationIds.current = editor.deltaDecorations(
        decorationIds.current,
        [
          {
            range: {
              startLineNumber: lineNumber,
              startColumn: 1,
              endLineNumber: lineNumber,
              endColumn: 1
            },
            options: {
              isWholeLine: true,
              className: "codelens-selected-line"
            }
          }
        ]
      );
    });
  }

  useEffect(() => {
    if (
      editorRef.current &&
      decorationIds.current.length > 0
    ) {
      editorRef.current.deltaDecorations(
        decorationIds.current,
        []
      );
    }

    decorationIds.current = [];

    setSelectedLine(null);
    setExplanation(null);
  }, [code]);

  useEffect(() => {
    if (!selectedLine) {
      return;
    }

    async function explainSelectedLine() {
      try {
        const response = await fetch(
          "http://127.0.0.1:8000/explain",
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json"
            },
            body: JSON.stringify({
              code: code,
              line_number: selectedLine
            })
          }
        );

        const data = await response.json();

        console.log("Backend response:", data);

        setExplanation(data.explanation);
      } catch (error) {
        console.error(
          "Backend connection failed:",
          error
        );
      }
    }

    explainSelectedLine();
  }, [selectedLine, code]);

  return (
    <div className="app">
      <header className="header">
        <div>
          <h1>🔍 CodeLens</h1>
          <p>Understand code, one line at a time.</p>
        </div>

        <span className="language">Python</span>
      </header>

      <main className="workspace">
        <section className="code-panel">
          <div className="panel-title">
            Python Code
          </div>

          <div className="editor-container">
            <Editor
              height="100%"
              defaultLanguage="python"
              value={code}
              onChange={(value) =>
                setCode(value || "")
              }
              onMount={handleEditorMount}
              theme="vs-light"
              options={{
                fontSize: 16,
                minimap: {
                  enabled: false
                },
                wordWrap: "on",
                automaticLayout: true,
                padding: {
                  top: 15
                }
              }}
            />
          </div>
        </section>

        <section className="explanation-panel">
          <div className="panel-title">
            💡 Explanation
          </div>

          {explanation ? (
            <div className="selected-line">
              <h2>Line {selectedLine}</h2>

              <h3>What</h3>
              <p>{explanation.what}</p>

              <h3>Why</h3>
              <p>{explanation.why}</p>

              <h3>Parts</h3>
              <ul>
                {explanation.parts.map(
                  (part, index) => (
                    <li key={index}>
                      {part}
                    </li>
                  )
                )}
              </ul>

              <h3>In simple words</h3>
              <p>{explanation.simple}</p>
            </div>
          ) : (
            <div className="empty-state">
              <h2>Select a line</h2>
              <p>
                Click a line of code to understand
                what it does and why it is needed.
              </p>
            </div>
          )}
        </section>
      </main>
    </div>
  );
}

export default App;