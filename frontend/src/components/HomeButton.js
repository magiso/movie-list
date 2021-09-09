import React from 'react';
import axios from 'axios';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import {
    IconButton
} from "@material-ui/core";
import Home from '@material-ui/icons/Home';

function HomeButton() {
    function handlePress(event) {
        // history push home
    }

    return (
        <div>
            <IconButton size = "small" onClick = {handlePress}>
                <Home />
            </IconButton>
        </div>
    )
}

export default HomeButton;