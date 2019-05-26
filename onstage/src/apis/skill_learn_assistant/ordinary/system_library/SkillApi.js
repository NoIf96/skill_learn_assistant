import * as API from '../../../'
import * as PrefixBase from '../system_library'

let base = PrefixBase.getBase() + 'skill/';

export default {
  getList: params => {
    return API.GET(base + 'list', params);
  },
  getUserList: params => {
    return API.GET(base + 'user_list', params);
  },
  saveUserSkill: params => {
    return API.POST(base + 'save_user_skill', params);
  }
}
