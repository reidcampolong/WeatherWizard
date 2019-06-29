import axios from 'axios';
const subscribeURL = "http://localhost:8080/subscribe/"

const axiosHeader = ({
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    }
  }
);

const sendSubscribe = (email: string, location: string) => {
  return axios.post(subscribeURL, {
      email: email,
      location: location,
  }, axiosHeader);
}

export default sendSubscribe;