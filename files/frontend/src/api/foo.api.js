
const BASE_URL = 'http://127.0.0.1:8000/api/';

const GET_REQUEST = {
    method: 'GET',
    credentials: 'include'
};

export async function getFooList() {
    const response = await fetch( BASE_URL + 'foo/', GET_REQUEST )
    const data = await response.json();
    return data.fooItemArray;
}
