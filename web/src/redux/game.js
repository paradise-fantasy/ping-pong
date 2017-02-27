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


    case 'MATCH_SETUP_EXPIRED':
      return {};

    case 'NEW_MATCH_STARTED':
      return {
        ...state,
        state: 'starting',
        isRanked: true,
        score1: 0,
        score2: 0,
        started: action.date,
        ratingGains: {
          player_1: { wins: 0, loses: 0 },
          player_2: { wins: 0, loses: 0 }
        }
      };

    case 'NEW_UNRANKED_MATCH_STARTED':
      return {
        ...state,
        state: 'starting',
        isRanked: false,
        player1: null,
        player2: null,
        score1: 0,
        score2: 0,
        started: action.date
      };

    case 'RECEIVE_MATCH_RATING_GAINS':
      return {
        ...state,
        ratingGains: action.ratingGains
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

    case 'MATCH_OVER':
      return {
        ...state,
        state: 'over'
      };

    case 'MATCH_CANCELLED':
      return {
        ...state,
        state: 'cancelled'
      }

    case 'RESET_MATCH':
      return {};

    default:
      return state;
  }
};

export {
  gameReducer
}
