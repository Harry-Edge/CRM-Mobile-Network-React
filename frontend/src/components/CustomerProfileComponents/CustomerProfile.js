import React, {Component} from "react";
import { withStyles } from '@material-ui/core/styles';

const styles = (theme) => ({
    textSuccess: {
        color: 'green'
    },
});

class CustomerProfile extends Component {

    render() {

        return (
           <div>
               <h1>CUSTOMER PROFILE</h1>
           </div>
        )
    }
}
export default withStyles(styles)(CustomerProfile)