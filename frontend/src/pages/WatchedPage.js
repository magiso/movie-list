import React from 'react';
import {List, ListItem, ListSubheader, ListItemText} from '@material-ui/core';
//import axios from 'axios';
import AddMovieBox from '../components/Watched/AddMovieBox';
import ClearWatchedBox from '../components/Watched/ClearWatchedBox';
import SwitchPageBox from '../components/Watched/SwitchPageBox';
import {Grid} from "@material-ui/core";

import {useStep} from '../utils/update';

function WatchedPage() {
    const axios = require('axios');
    const [WatchedData, setWatchedData] = React.useState([]);

    const fetchMovieList = () => {
        axios.get('http://127.0.0.1:8000/watched/list').then(response => {
            console.log(response.data);
            setWatchedData(response.data.watched_list);
        });
    }

    useStep(fetchMovieList, [], 2);

    return (
        <div>
            <h1> Watched List! </h1>
            <Grid
                container
                spacing={1}
                direction="row"
                justify="left"
                alignItems="center"
            >
                <SwitchPageBox />
                <AddMovieBox callback = {fetchMovieList} />
                <ClearWatchedBox callback = {fetchMovieList} />
            </Grid>
            
            <List subheader = {
                <ListSubheader style={{ display: 'flex' }}>
                    <span style={{ flex: 1 }}> My Movies to Watch </span>
                </ListSubheader>
            }>
                {WatchedData.map(({name, year, genre, date_watched, score}, index) => (
                    <ListItem>
                        <span>
                            <ListItemText primary ={name} />
                            <ListItemText primary ={year} />
                            <ListItemText primary ={genre} />
                            <ListItemText primary ={date_watched} />
                            <ListItemText primary ={score} />
                        </span>    
                    </ListItem>
                ))}
            </List>
        </div>
    )
}

export default WatchedPage;