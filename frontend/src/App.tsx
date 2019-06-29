import React, { useState } from 'react';
import SubscribeView from './components/SubscribeView';
import SuccessView from './components/SuccessView';

const App: React.FC = () => {
  const [hasSubmitted, setSubmitted] = useState<boolean>(false);

  return (
    <div>
      {hasSubmitted ? <SuccessView/> : <SubscribeView setSubmitted={setSubmitted}/>}
    </div>
  );
};

export default App;
