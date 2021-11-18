import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movieCards: [],
    mylists: []
  },

  mutations: {
    LOAD_MOVIE_CARDS: function (state, results) {
      state.movieCards = results
    },

    CREATE_MYLIST: function (state, myListItem) {
      state.mylists.push(myListItem)
    },
  },
  actions: {
    LoadMovieCards: function ({ commit }) {
      axios({
        method: 'get',
        url: 'https://api.themoviedb.org/3/movie/top_rated',
        params: {
          api_key: '###',
          language: 'ko-KR',
        }
      })

        .then((res) => {
          console.log(res)
          commit('LOAD_MOVIE_CARDS', res.data.results)
        })
      },

      createMylist: function ({ commit }, myListItem) {
        commit('CREATE_MYLIST', myListItem)
      },
    
  },
  modules: {
  }
})