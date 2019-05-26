import * as API from '../../'
import * as PrefixBase from '../'

let base = PrefixBase.getBase() + 'auth/';

export default {
  login: params => {
    return API.POST_FORM(base + 'login', params);
  },
  logout: params => {
    return API.GET(base + 'logout', params);
  },
  getCurrentUser: params => {
    return API.GET(base + 'get_current_user', params);
  },
  register: params => {
    return API.POST_FORM(base + 'register', params)
  }
}
