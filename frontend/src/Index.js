import App from "./components/App";
import React, { Component } from "react";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import store from "./store";
export default class Index extends Component {
    render() {
        return (
            <Provider store={store}>
                <App />
            </Provider>
        );
    }
}
ReactDOM.render(<Index />, document.getElementById("Root"));
