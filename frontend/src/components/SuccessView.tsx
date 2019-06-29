import React from 'react';
import { Container } from 'reactstrap';
import styled from 'styled-components';

const StyledContainer = styled(Container)`
    margin-top: 40px;
    padding: 20px;
    max-width: 320px;
    border: 1px solid black;
`;

const SuccessView = () => {
  return (
    <StyledContainer className="App">
      <h2>Weather Powered Email</h2>
      Thanks for submitting!
    </StyledContainer>
  );
}

export default SuccessView;