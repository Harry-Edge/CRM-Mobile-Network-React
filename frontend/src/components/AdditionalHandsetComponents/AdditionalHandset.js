import React, {Component} from "react";
import { withStyles } from '@material-ui/core/styles';
import Typography from "@material-ui/core/Typography";

const styles = (theme) => ({
    textSuccess: {
        color: 'green'
    },
});

class AdditionalHandset extends Component {

    render() {

        return (
           <div>
               <h1>ADDITIONAL HANDSET</h1>
           </div>
        )
    }
}
export default withStyles(styles)(AdditionalHandset)