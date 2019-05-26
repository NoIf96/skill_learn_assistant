import * as API from '../../../'
import * as PrefixBase from '../user'

let base = PrefixBase.getBase() + 'ordinary/';

export default {
  add: params => {
    return API.POST(base + 'add', params);
  },
  del: params => {
    return API.POST(base + 'delete', params);
  },
  edit: params => {
    return API.POST(base + 'edit', params);
  },
  getList: params => {
    return API.GET(base + 'list', params);
  }
}
