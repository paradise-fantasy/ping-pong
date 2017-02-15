import React, { Component } from 'react';
import { FormGroup, Button, FormControl, ControlLabel, Form, Col, HelpBlock } from 'react-bootstrap';
import { browserHistory } from 'react-router';

import PageHeader from '../PageHeader';

import './style.css';

const HTTPS_ENABLED = !!process.env.REACT_APP_HTTPS_ENABLED;
const API_HOST = process.env.REACT_APP_API_HOST || 'localhost';
const API_PORT = process.env.REACT_APP_API_PORT || 8000;
const API_URL = `${HTTPS_ENABLED ? 'https' : 'http'}://${API_HOST}:${API_PORT}`;

function postNewPlayer(form) {
    return fetch(`${API_URL}/players/`, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(form)
    })
    .catch (function (error) {
        console.log("Request failed", error)
    })
}

class RegisterForm extends Component {

    constructor(props) {
        super(props);
        this.state = {
            name: '',
            cardid: '',
            profile_picture: '',
            error: {},
            success: false
        };
        this.handleSubmit = this.handleSubmit.bind(this)
        this.handleInputChange = this.handleInputChange.bind(this)
    }

    componentDidMount() {
    }
    componentWillUnmount() {
    }

    handleInputChange(event) {
        const target = event.target;
        const value = target.value;
        const name = target.name;

        this.setState({
            [name]: value
        });
    }

    handleSubmit(event) {
        const { name, cardid, profile_picture } = this.state;
        const form = { name, cardid, profile_picture };

        postNewPlayer(form)
        .then((response) => {
            if ( response.status !== 201 ) {
                response.json()
                .then(error => this.setState({ error }))
            } else {
                this.setState({
                    success: true
                });
                setTimeout(browserHistory.goBack, 3000)
            }
        });
        event.preventDefault();
    }

    render() {
        return (
            <div className="Register">
                <PageHeader headerText="Komstek Ping Pong League" />
                <Col md={8} mdOffset={2} >
                    <h1>{this.state.info}</h1>
                    { !this.state.success ?
                        <Form horizontal>
                            <FormGroup controlId="formHorizontalName">
                                <Col componentClass={ControlLabel} md={2}>
                                    Name
                                </Col>
                                <Col md={10}>
                                    <FormControl
                                        name="name"
                                        type="text"
                                        placeholder="Enter your name"
                                        value={this.state.name}
                                        onChange={this.handleInputChange}
                                    />
                                    {this.state.error.name ?
                                        <HelpBlock className="api-error">
                                            {this.state.error.name.join(" ")}
                                        </HelpBlock>
                                    :
                                        null
                                    }
                                </Col>
                            </FormGroup>
                            <FormGroup controlId="formHorizontalCardId">
                                <Col componentClass={ControlLabel} md={2}>
                                    Card ID
                                </Col>
                                <Col md={10}>
                                    <FormControl
                                        name="cardid"
                                        type="text"
                                        placeholder="Enter your card ID"
                                        value={this.state.cardid}
                                        onChange={this.handleInputChange}
                                    />
                                    <HelpBlock className="text-left">
                                        Download <a href="https://play.google.com/store/apps/details?id=com.wakdev.wdnfc">NFC Tools</a> for Android to find your card ID. The app shows your ID as <b>"Serial number"</b>. We only accept the ID on the form <b>AA11BB22</b> <u>NOT</u> AA:11:BB:22.
                                    </HelpBlock>
                                    {this.state.error.cardid ?
                                        <HelpBlock className="api-error">
                                            {this.state.error.cardid.join(" ")}
                                        </HelpBlock>
                                    :
                                        null
                                    }
                                </Col>
                            </FormGroup>
                            <FormGroup controlId="formHorizontalProfilePicture">
                                <Col componentClass={ControlLabel} md={2}>
                                    Profile Picture
                                </Col>
                                <Col md={10}>
                                    <FormControl
                                        name="profile_picture"
                                        type="text"
                                        placeholder="Paste a link to your profile picture"
                                        value={this.state.profile_picture}
                                        onChange={this.handleInputChange}
                                    />
                                {this.state.error.profile_picture ?
                                    <HelpBlock className="api-error">
                                        {this.state.error.profile_picture.join(" ")}
                                    </HelpBlock>
                                :
                                    null
                                }
                                </Col>
                            </FormGroup>
                            <Button
                                bsSize="lg"
                                type="submit"
                                value="Submit"
                                onClick={this.handleSubmit}
                            >
                                Submit
                            </Button>
                        </Form>
                    : // If form has been successfully posted
                        <h1>
                            {this.state.name} has been successfully registered!<br/>
                            Redirecting you to front page.
                        </h1>
                    }
                </Col>
            </div>
        )
    }
}

export default RegisterForm
