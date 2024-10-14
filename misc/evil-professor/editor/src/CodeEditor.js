import { useState, useEffect } from 'react'
import CodeMirror, { EditorView } from '@uiw/react-codemirror';
import { dracula } from '@uiw/codemirror-theme-dracula'
import { python } from '@codemirror/lang-python';

const CodeEditor = () => {
  const [code, setCode] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetch('/starter.py')
      .then(response => response.text())
      .then(text => setCode(text))
  }, []);

  const submit = async () => {
    setLoading(true);

    await fetch(`http://${window.location.host}/api/test-code`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({code: code})
    })
      .then(async response => await response.json())
      .then(json => setResult(json))
      .then(() => setLoading(false));
  };

  return (
    <div className='container'>
      <h1>CSCE 437 - Programming Assignment 1</h1>
      <div className='editor-results'>
        <div className='editor'>
          <CodeMirror
            className='editor'
            width='100%'
            height='100%'
            value={code}
            onChange={value => setCode(value)}
            theme={dracula}
            extensions={[python(), EditorView.lineWrapping]}
          />
        </div>
        <div className='test-results'>
          <h2>Test Results</h2>
          <button disabled={loading} onClick={submit}>Run Tests</button>
          <CodeMirror
            className='output'
            width='100%'
            height='100%'
            maxHeight='100%'
            value={
              result ?
                Object.keys(result).map(key => {
                  return `${key}: ${result[key]}`
                }).join('\n')
              : ''}
            theme={dracula}
            extensions={[EditorView.lineWrapping]}
          />
        </div>
      </div>
    </div>
  );
};

export default CodeEditor;
