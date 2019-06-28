import React, { useState } from 'react';
import {
  Container, Col, Form,
  FormGroup, Label, Input,
  Button, Dropdown, DropdownToggle, DropdownMenu, DropdownItem
} from 'reactstrap';
import styled from 'styled-components';

const StyledContainer = styled(Container)`
    margin-top: 40px;
    padding: 20px;
    max-width: 320px;
    border: 1px solid black;
`;

const SignupView = () => {
  const [dropdownIsOpen, setDropDownOpen] = useState<boolean>(false);

  return (
    <StyledContainer className="App">
    <h2>Weather Powered Email</h2>
    <Form className="form">
      <Col>
        <FormGroup>
          <Label>Email Address</Label>
          <Input
            type="email"
            name="email"
            placeholder="weather@klaviyo.com"
          />
        </FormGroup>
      </Col>
      <Col>
        <FormGroup>
          <Dropdown isOpen={dropdownIsOpen} toggle={() => setDropDownOpen(!dropdownIsOpen)}>
          <DropdownToggle color="info" caret>
            Choose your location
          </DropdownToggle>
          <DropdownMenu>
            
          </DropdownMenu>
          </Dropdown>
        </FormGroup>
      </Col>
      <Button>Submit</Button>
    </Form>
  </StyledContainer>
  );
}

export default SignupView;