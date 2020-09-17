import App from "./components/App";
import React, { Component } from "react";
import ReactDOM from "react-dom";
export default class Index extends Component {
    render() {
        return (
            <div>
                <App />
            </div>
        );
    }
}
ReactDOM.render(<Index />, document.getElementById("Root"));
