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
    Switch,
    TextField,
    Grid,
    FormControlLabel,
} from "@material-ui/core";
import Delete from "@material-ui/icons/Delete";

function AddClearBox({...props}) {
    const [open, setOpen] = React.useState(false);
    function handleClickOpen() {
        setOpen(true);
    }
    function handleClose() {
        setOpen(false);
    }
    function handleConfirm(event) {
        axios.delete('http://127.0.0.1:8000/towatch/clear')
        .then(response => {
            console.log(response);
            props.callback();
        });
        handleClose();
    }

    return (
        <div>
            <IconButton size = "small" onClick = {handleClickOpen}>
                <Delete />
            </IconButton>
            <Dialog
                open={open}
                onClose={handleClose}
                aria-labelledby="form-dialog-title"
            >
                <DialogTitle id="form-dialog-title"> Clear all movies from this list? </DialogTitle>
                <DialogContentText>
                    Are you sure you want to clear all movies? This cannot be undone.
                </DialogContentText>
                <DialogActions>
                    <Button onClick={handleClose} color="primary">
                        Cancel
                    </Button>
                    <Button onClick={handleConfirm} type="submit" color="primary">
                        Clear All
                    </Button>
                </DialogActions>
            </Dialog>
        </div>
    )
}

export default AddClearBox;