import React, { useState } from 'react';
import {
  Container, Col, Form,
  FormGroup, Label, Input,
  Button
} from 'reactstrap';
import DropDown from './DropDown';
import sendSubscribe from '../data/DatabaseSender';
import styled from 'styled-components';

const StyledContainer = styled(Container)`
    margin-top: 40px;
    padding: 20px;
    max-width: 320px;
    border: 1px solid black;
`;

interface ISignupView {
  readonly setResponse: React.Dispatch<React.SetStateAction<string | undefined>>;
}

const SignupView: React.FC<ISignupView> = ({ setResponse }) => {
  const [email, setEmail] = useState<string>('');
  const [location, setLocation] = useState<string>('');

  const onFormSubmit = (e: any) => {
    e.preventDefault();
    sendSubscribe(email, location).then(({ data }) => {
      setResponse(data);
    }).catch(error =>
      setResponse("You are already registered with us! Keep your eye out for our emails")
    );
  }
  
  return (
    <StyledContainer className="App">
      <h2>Weather Powered Email</h2>
      <Form onSubmit={(e) => onFormSubmit(e)}>
        <Col>
          <FormGroup>
            <Label>Email Address</Label>
            <Input
              type="email"
              name="email"
              placeholder="weather@klaviyo.com"
              onChange={(e) => setEmail(e.target.value)}
            />
          </FormGroup>
        </Col>
        <Col>
          <FormGroup>
            <DropDown placeholder="Select your location..." setDropDownSelect={setLocation} />
          </FormGroup>
        </Col>
        <Button>Subscribe</Button>
      </Form>
    </StyledContainer>
  );
}

export default SignupView;