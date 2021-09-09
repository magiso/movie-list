import React from 'react';
import axios from 'axios';
import {
    Dialog,
    DialogTitle,
    DialogActions,
    DialogContent,
    DialogContentText,
    IconButton,
    Button,
    TextField,
    Grid,
} from "@material-ui/core";
import Add from "@material-ui/icons/Add";

function AddMovieBox({...props}) {
    const [open, setOpen] = React.useState(false);
    function handleClickOpen() {
        setOpen(true);
    }
    function handleClose() {
        setOpen(false);
    }
    function handleSubmit(event) {
        event.preventDefault();
        const name = event.target[0].value;
        const year = event.target[1].value;
        const genre = event.target[2].value;

        if (!name) return;

        axios.post('http://127.0.0.1:8000/towatch/new', {name, year, genre})
        .then(response => {
            console.log(response.data);
            props.callback();
        })
        .catch(err => { });
 
    }

    return (
        <div>
            <IconButton size="small" onClick={handleClickOpen}>
                <Add />
            </IconButton>
            <Dialog
                open={open}
                onClose={handleClose}
                aria-labelledby="form-dialog-title"
            >
                <DialogTitle id="form-dialog-title"> Add a new  movie </DialogTitle>
                <form onSubmit={handleSubmit}>
                    <DialogContent>
                        <DialogContentText>
                            Fill in movie details
                        </DialogContentText>
                        <Grid
                            container
                            spacing={3}
                            direction="row"
                            justify="center"
                            alignItems="center"
                            >
                            <Grid item xs={12}>
                                <TextField
                                    autoFocus
                                    margin="dense"
                                    id="name"
                                    label="Movie Name"
                                    name="name"
                                    fullWidth
                                />
                            </Grid>
                            <Grid item xs={12}>
                                <TextField
                                    autoFocus
                                    margin="dense"
                                    id="year"
                                    label="Movie Year"
                                    name="year"
                                    fullWidth
                                />
                            </Grid>
                            <Grid item xs={12}>
                                <TextField
                                    autoFocus
                                    margin="dense"
                                    id="genre"
                                    label="Movie Genre"
                                    name="genre"
                                    fullWidth
                                />
                            </Grid>
                            <Grid item xs={12}>
                                <TextField
                                    autoFocus
                                    margin="dense"
                                    id="date"
                                    label="Date Watched"
                                    name="date"
                                    fullWidth
                                />
                            </Grid>
                            <Grid item xs={12}>
                                <TextField
                                    autoFocus
                                    margin="dense"
                                    id="score"
                                    label="Movie Score"
                                    name="score"
                                    fullWidth
                                />
                            </Grid>
                        </Grid>
                    </DialogContent>
                    <DialogActions>
                        <Button onClick={handleClose} color="primary">
                            Cancel
                        </Button>
                        <Button onClick={handleClose} type="submit" color="primary">
                            Create
                        </Button>
                    </DialogActions>
                </form> 
            </Dialog>
        </div>
    )
}


export default AddMovieBox;