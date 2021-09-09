import React from 'react';
import {List, ListItem, ListSubheader, ListItemText} from '@material-ui/core';
//import axios from 'axios';
import AddMovieBox from '../components/ToWatch/AddMovieBox';
import ClearToWatchBox from '../components/ToWatch/ClearToWatchBox';
import SwitchPageBox from '../components/ToWatch/SwitchPageBox';
import HomeButton from '../components/HomeButton';
import {Grid} from "@material-ui/core";

import {useStep} from '../utils/update';

function ToWatchPage() {
    const axios = require('axios');
    const [toWatchData, setToWatchData] = React.useState([]);

    const fetchMovieList = () => {
        axios.get('http://127.0.0.1:8000/towatch/list').then(response => {
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
                <HomeButton />
                <SwitchPageBox />
                <AddMovieBox callback = {fetchMovieList} />
                <ClearToWatchBox callback = {fetchMovieList} />
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

export default ToWatchPage;