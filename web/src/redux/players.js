import { keyBy } from 'lodash';

const playersReducer = (state = {}, action) => {
  switch (action.type) {
    case 'RECEIVE_PLAYERS':
      return {
        list: action.players.slice(0),
        map: keyBy(action.players, 'cardid')
      };
    default:
      return state;
  }
};

export {
  playersReducer
}
