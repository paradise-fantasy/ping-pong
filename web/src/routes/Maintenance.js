import React, { Component } from 'react';


class Maintenance extends Component {
  render() {
    return (
      <div className="Maintenance">
        <div className="Main-text-maintenance">
          <h1>Maintenance</h1>
	  <h2>The system has been put into maintenance mode</h2>
        </div>
	<div className="Main-text-maintenance">
	    
	    <h3>Issue: </h3>
	    <p> {this.props.location.query.issue}</p>
	    <br />
	    <h3>Start:</h3>
	    <p>{this.props.location.query.start}</p>
	    <br/>
	    <h3>End:</h3>
	    <p>{this.props.location.query.stop}</p>
	    <br />
	    <p>We apologize for any inconveniences that this may cause you!</p><br />
	    <p>Enquiries regarding the maintenance can be sendt to Paradise (A-187)</p>
	</div>
      </div>
    )
  }
}

export default Maintenance;
