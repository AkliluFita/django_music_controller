import { render } from "react-dom";
import React from "react";

function App() {
  return (
    <div>
      <h1>hello i am react app(funcational based component)</h1>
    </div>
  );
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
