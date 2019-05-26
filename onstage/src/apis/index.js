/**
 * Created by yqr on 2018/4/13.
 */
import axios from 'axios'

axios.defaults.withCredentials = true;

// let base = 'http://127.0.0.1:5000/api/';
let base = 'http://47.94.197.39:8000/api/';

export const getBase = () => {
  return base
};

export const POST = (url, params) => {
  return axios.post(url, params).then(res => res.data)
};

export const POST_FORM = (url, params) => {
  // params.append('csrf_token', getCookie('csrf_token'));
  return axios.post(url, params, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  }).then(res => res.data)
};

export const GET = (url, params) => {
  return axios.get(url, {params: params}).then(res => res.data)
};

export const PUT = (url, params) => {
  return axios.put(url, params).then(res => res.data)
};

export const DELETE = (url, params) => {
  return axios.delete(url, {params: params}).then(res => res.data)
};

export const PATCH = (url, params) => {
  return axios.patch(url, params).then(res => res.data)
};

export function getCookie (name) {
  let reg = new RegExp('(^| )' + name + '=([^;]*)(;|$)');
  let arr = document.cookie.match(reg);
  if (arr) {
    return (arr[2]);
  }
  return null;
}
