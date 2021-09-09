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
    const [toWatchData, setToWatchData] = React.useState([]);

    const fetchMovieList = () => {
        axios.get('http://127.0.0.1:8000/watched/list').then(response => {
            console.log(response.data);
            //console.log(response.data.to_watch_list[1].name);
            // for(let i = 0; i < 2; i++) {
            //     data.push(response.data.to_watch_list[i].name);
            // }
            
            setToWatchData(response.data.to_watch_list);
        });
    }

    useStep(fetchMovieList, [], 2);

    return (
        <div>
            <h1> To Watch List! </h1>
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
                {toWatchData.map(({name, year, genre}, index) => (
                    <ListItem>
                        <span>
                            <ListItemText primary ={name} />
                            <ListItemText primary ={year} />
                            <ListItemText primary ={genre} />
                        </span>    
                    </ListItem>
                ))}
            </List>
        </div>
    )
}

export default WatchedPage;