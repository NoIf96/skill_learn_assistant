import * as API from '../../../'
import * as PrefixBase from '../system_library'

let base = PrefixBase.getBase() + 'occupation/';

export default {
  getList: params => {
    return API.GET(base + 'list', params);
  }
}
