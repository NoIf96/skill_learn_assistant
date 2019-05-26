import crypto from 'crypto-js'

const key = '1234567891234567';

function aesEncrypt (data) {
  console.info('11');
  const cipher = crypto.createCipher('aes192', key);
  let crypted = cipher.update(data, 'utf8', 'hex');
  crypted += cipher.final('hex');
  console.info(crypted);
  return crypted;
}

function aesDecrypt (encrypted) {
  const decipher = crypto.createDecipher('aes192', key);
  let decrypted = decipher.update(encrypted, 'hex', 'utf8');
  decrypted += decipher.final('utf8');
  return decrypted;
}

export default {aesEncrypt, aesDecrypt}
