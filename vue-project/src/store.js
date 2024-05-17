import { createStore } from 'vuex';

export default createStore({
  state: {
    deletedUsers: [], 
  },
  mutations: {
    addUserToDeleted(state, userId) {
      state.deletedUsers.push(userId);
    },
    removeUserFromDeleted(state, userId) {
      state.deletedUsers = state.deletedUsers.filter(id => id !== userId);
    },
  },
  actions: {
    addUserToDeleted({ commit }, userId) {
      commit('addUserToDeleted', userId);
    },
    removeUserFromDeleted({ commit }, userId) {
      commit('removeUserFromDeleted', userId);
    },
  },
});
