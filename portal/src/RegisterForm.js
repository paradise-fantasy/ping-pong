import React, { Component } from 'react';
import { FormGroup, Button, FormControl, ControlLabel, Form, Col, Row } from 'react-bootstrap';

class RegisterForm extends Component {

    constructor(props) {
        super(props);
        this.state = {
            date: new Date(),
            name: 'Enter name',
            cardid: 'Enter your card ID',
            profile_picture: 'Paste a link to your profile picture'
        };
        
    }

    componentDidMount() {
        this.timerID = setInterval(
            () => this.tick(),
            1000
        )
    }
    componentWillUnmount() {
        clearInterval(this.timerID);
    }

    tick() {
        this.setState({
            date: new Date()
        });
    }

    handleInputChange(event) {

        this.setState({

        });
    }

    handleSubmit(event) {

    }


    render() {
        return (

            <div>
                <h1>{this.state.info}</h1>
                <Form horizontal>
                    <FormGroup controlId="formHorizontalName">
                        <Col componentClass={ControlLabel} md={3}>
                            Name
                        </Col>
                        <Col md={9}>
                            <FormControl type="text" placeholder="Enter name" />
                        </Col>
                    </FormGroup>
                    <FormGroup controlId="formHorizontalCardId">
                        <Col componentClass={ControlLabel} md={3}>
                            Card ID
                        </Col>
                        <Col md={9}>
                            <FormControl type="text" placeholder="Enter your card ID" />
                        </Col>
                    </FormGroup>
                    <FormGroup controlId="formHorizontalProfilePicture">
                        <Col componentClass={ControlLabel} md={3}>
                            Profile Picture
                        </Col>
                        <Col md={9}>
                            <FormControl type="text" placeholder="Paste a link to your profile picture" />
                        </Col>
                    </FormGroup>

                    <Button bsSize="lg" type="submit">
                        Submit
                    </Button>
                </Form>
            </div>
        )
    }
}



export default RegisterForm
