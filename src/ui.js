/**
 * 在点的名字变化时，自动填上 x 和 y
 */
function onPointNameInput() {
    let name = document.getElementById('point-name').value;
    let inputPointX = document.getElementById('point-x');
    let inputPointY = document.getElementById('point-y');
    if (name !== '') {
        inputPointX.value = `x_{${name}}`;
        inputPointY.value = `y_{${name}}`;
    } else {
        inputPointX.value = '';
        inputPointY.value = '';
    }
}