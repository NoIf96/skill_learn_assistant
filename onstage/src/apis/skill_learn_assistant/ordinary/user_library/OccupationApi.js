import * as API from '../../../'
import * as PrefixBase from '../user_library'

let base = PrefixBase.getBase() + 'occupation/';

export default {
  getUserList: params => {
    return API.GET(base + 'list', params);
  }
}
