const statusMessagesReducer = (state = [], action) => {
  switch (action.type) {
    case 'RECEIVE_STATUS':
      return [
        ...state,
        action.data
      ];

    case 'REMOVE_STATUS':
      return state.filter(status => status.id !== action.data);

    case 'CLEAR_STATUS_GROUP':
      return state.filter(status => status.group !== action.data);

    default:
      return state;
  }
};

export {
  statusMessagesReducer
}
