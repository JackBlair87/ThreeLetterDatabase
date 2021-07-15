//Jack Blair 
// API Reference: https://www.wix.com/velo/reference/api-overview/introduction

let colors = ['#EC8767', '#4793A3', '#4E9E31', '#C42F2F']

$w.onReady(function () {
	let dataArray = $w("#listRepeater").data
	const shuffledArray = shuffleArray(dataArray);
	$w('#listRepeater').data = shuffledArray;
});

function getRandomIndex(min, max) {
    return Math.round(Math.random() * (max - min) + min);
}

function shuffleArray(dataArray){
	for(let i = dataArray.length - 1; i > 0; i--){
		let index = getRandomIndex(0, i);
		const temp = dataArray[i];
		dataArray[i] = dataArray[index];
		dataArray[index] = temp;
	}
	
	return dataArray;
}

/**
 *	Sets the function that runs when a new repeated item is created.
 *	 @param {$w.$w} $item,
 *	 @param {Object} itemData,
 *	 @param {Number} index
 */
export function listRepeater_itemReady($item, itemData, index) {
	$w("#listRepeater").forEachItem( ($w, itemData, index) => {
		let color = colors[getRandomIndex(0, 3)];
		let word = itemData['title'].replace("\"", '')
		$w("#box18").style.backgroundColor = color;
		$w("#text1").html = '<h3 style="font-size:40px; text-align:center"><span style="color:' + color + '"><span style="font-size:40px"><span style="font-family:worksans-semibold,work sans,sans-serif">' + word + '</span></span></span></h3>'
	});
}
