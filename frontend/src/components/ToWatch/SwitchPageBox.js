import React from 'react';
import axios from 'axios';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import {
    IconButton
} from "@material-ui/core";
import CompareArrowsIcon from '@material-ui/icons/CompareArrows';

function SwitchPageBox() {
    function handlePress(event) {
        // history
        // history.push(watched page)
    }

    return (
        <div>
            <IconButton size = "small" onClick = {handlePress}>
                <CompareArrowsIcon />
            </IconButton>
        </div>
    );
}


export default SwitchPageBox;