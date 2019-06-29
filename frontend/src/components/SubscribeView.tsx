import React, { useState } from 'react';
import {
  Container, Col, Form,
  FormGroup, Label, Input,
  Button
} from 'reactstrap';
import DropDown from './DropDown';
import sendSubscribe from './DatabaseSender';
import styled from 'styled-components';

const StyledContainer = styled(Container)`
    margin-top: 40px;
    padding: 20px;
    max-width: 320px;
    border: 1px solid black;
`;

const SignupView = () => {
  const [email, setEmail] = useState<string>('');
  const [location, setLocation] = useState<string>('');

  const onFormSubmit = (e: React.FormEvent) => {
    sendSubscribe(email, location);
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
            <DropDown placeholder="Select your location..." setDropDownSelect={setLocation}/>
          </FormGroup>
        </Col>
        <Button>Submit</Button>
      </Form>
    </StyledContainer>
  );
}

//<Dropdown suggestions={cities} isOpen={dropdownIsOpen} toggle={() => setDropDownOpen(!dropdownIsOpen)}>

export default SignupView;