import * as API from '../../../'
import * as PrefixBase from '../user'

let base = PrefixBase.getBase() + 'admin/';

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
  },
  getPermissionOptions: params => {
    return API.GET(base + 'get_permission_options', params);
  }
}
