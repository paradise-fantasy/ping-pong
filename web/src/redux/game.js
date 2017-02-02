const gameReducer = (state = {}, action) => {
  switch (action.type) {
    case 'PLAYER_1_JOINED':
      return {
        ...state,
        player1: action.cardId
      };

    case 'PLAYER_2_JOINED':
      return {
        ...state,
        player2: action.cardId
      };

    case 'NEW_MATCH_STARTED':
      return {
        ...state,
        state: 'starting',
        score1: 0,
        score2: 0,
        started: action.date
      };

    case 'NEW_URANKED_MATCH_STARTED':
      return {
        ...state,
        state: 'starting',
        player1: null,
        player2: null,
        score1: 0,
        score2: 0,
        started: action.date
      };

    case 'MATCH_INTRO_OVER':
      return {
        ...state,
        state: 'started'
      };

    case 'PLAYER_1_SCORE_INC':
      return {
        ...state,
        score1: state.score1 + 1
      };

    case 'PLAYER_1_SCORE_DEC':
      return {
        ...state,
        score1: state.score1 - 1
      };

    case 'PLAYER_2_SCORE_INC':
      return {
        ...state,
        score2: state.score2 + 1
      };

    case 'PLAYER_2_SCORE_DEC':
      return {
        ...state,
        score2: state.score2 - 1
      };

    case 'MATCH_CANCELLED':
    case 'MATCH_OVER':
      return {};

    default:
      return state;
  }
};

export {
  gameReducer
}
