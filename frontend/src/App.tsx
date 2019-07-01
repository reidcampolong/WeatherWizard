import React, { useState } from 'react';
import SubscribeView from './components/SubscribeView';
import SuccessView from './components/SuccessView';

const App: React.FC = () => {
  const [response, setResponse] = useState<string>();

  return (
    <div>
      {response ? <SuccessView response={response} /> : <SubscribeView setResponse={setResponse} />}
    </div>
  );
};

export default App;
