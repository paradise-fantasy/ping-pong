const API_HTTPS_ENABLED = !!process.env.REACT_APP_API_HTTPS_ENABLED;
const API_HOST = process.env.REACT_APP_API_HOST || 'localhost';
const API_PORT = process.env.REACT_APP_API_PORT || 8000;
const API_URL = `${API_HTTPS_ENABLED ? 'https' : 'http'}://${API_HOST}:${API_PORT}`;

const request = (url, options) =>
  fetch(`${API_URL}${url}`, options)
  .then(res => res.json());

const postRequest = (url, body, options) =>
  request(url, {
    method: 'POST',
    headers: { 'Content-Type': 'Application/JSON' },
    body: JSON.stringify(body),
    ...options
  });

const getRequest = (url, options) =>
  request(url, {
    method: 'GET',
    ...options
  });


const getPlayers = () => getRequest('/players/');
const getPlayerRatingGains = (id1, id2) => getRequest(`/players/${id1}/${id2}`);

export {
  request,
  getRequest,
  postRequest,
  getPlayers,
  getPlayerRatingGains,
  
}
