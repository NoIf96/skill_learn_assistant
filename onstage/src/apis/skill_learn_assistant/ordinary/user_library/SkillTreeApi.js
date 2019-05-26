import * as API from '../../../'
import * as PrefixBase from '../user_library'

let base = PrefixBase.getBase() + 'skill_tree/';

export default {
  getList: params => {
    return API.GET(base + 'list', params);
  }
}
