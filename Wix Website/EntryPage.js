//Jack Blair
import wixData from 'wix-data';
// API Reference: https://www.wix.com/velo/reference/api-overview/introduction

$w.onReady(function () {
	$w('#text31').text = "";
	$w('#text33').text = "";
	$w('#text34').text = "";

	$w('#text55').text = "";
	$w('#text53').text = "";
	$w('#text52').text = "";

	$w('#text59').text = "";
	$w('#text57').text = "";
	$w('#text56').text = "";

	$w('#text63').text = "";
	$w('#text61').text = "";
	$w('#text60').text = "";

	$w("#dynamicDataset").onReady( () => { //Get the current acronym
		let itemObj = $w("#dynamicDataset").getCurrentItem();
		let currentAcronym = itemObj['title']
		console.log(currentAcronym)
		$w("#dataset2").onReady( () => { 
            //Hide and unhide content panes depending on database entries
			testForResults(currentAcronym);
			setStockPanel(currentAcronym);
			setCollegePanel(currentAcronym);
			setAirportPanel(currentAcronym);
			setOrganizationPanel(currentAcronym);
  		} );
  	} );
});

function setStockPanel(acronym){
	const filter1 = wixData.filter()
	.contains("acronym", acronym)
	.startsWith("type", "Stock");

	wixData.aggregate("OrganizationEntries")
	.filter(filter1)
	.run()
	.then( (results) => {
		if (results.items.length > 0) {
			for(let x = 0; x < results.items.length; x++){
                let stock = results.items[x];
                console.log("Stock Item is", stock)
                $w('#text31').text = stock['title'];
                $w('#text33').text = String(stock['link']);
                $w('#text34').text = stock['description'];
                $w('#box8').expand()
			}
		} else {
		    // handle case where no matching items found
            //Since the pane is set to hidden by default we do nothing
		}
	} )
	.catch( (error) => {
		let errorMsg = error.message;
		let code = error.code;
	} );
}

function setCollegePanel(acronym){
	const filter1 = wixData.filter()
	.contains("acronym", acronym)
	.startsWith("type", "College");

	wixData.aggregate("OrganizationEntries")
	.filter(filter1)
	.run()
	.then( (results) => {
		if (results.items.length > 0) {
			for(let x = 0; x < results.items.length; x++){
                let stock = results.items[x];
                console.log("College Item is", stock)
                $w('#text55').text = stock['title'];
                $w('#text53').text = String(stock['link']);
                $w('#text52').text = stock['description'];
                $w('#box18').expand()
			}
		} else {
		    // handle case where no matching items found
            //Since the pane is set to hidden by default we do nothing
		}
	} )
	.catch( (error) => {
		let errorMsg = error.message;
		let code = error.code;
	} );
}

function setAirportPanel(acronym){
	const filter1 = wixData.filter()
	.contains("acronym", acronym)
	.startsWith("type", "Airport");

	wixData.aggregate("OrganizationEntries")
	.filter(filter1)
	.run()
	.then( (results) => {
		if (results.items.length > 0) {
			for(let x = 0; x < results.items.length; x++){
                let stock = results.items[x];
                console.log("Airport Item is", stock)
                $w('#text59').text = stock['title'];
                $w('#text57').text = String(stock['link']);
                $w('#text56').text = stock['description'];
                $w('#box19').expand()
			}
		} else {
		    // handle case where no matching items found
            //Since the pane is set to hidden by default we do nothing
		}
	} )
	.catch( (error) => {
		let errorMsg = error.message;
		let code = error.code;
	} );
}

function setOrganizationPanel(acronym){
	const filter1 = wixData.filter()
	.contains("acronym", acronym)
	.startsWith("type", "Organization");

	wixData.aggregate("OrganizationEntries")
	.filter(filter1)
	.run()
	.then( (results) => {
		if (results.items.length > 0) {
			for(let x = 0; x < results.items.length; x++){
                let stock = results.items[x];
                console.log("Organization Item is", stock)
                $w('#text63').text = stock['title'];
                $w('#text61').text = String(stock['link']);
                $w('#text60').text = stock['description'];
                $w('#box20').expand()
			}
		} else {
            // handle case where no matching items found
			//Since the pane is set to hidden by default we do nothing
		}
	} )
	.catch( (error) => {
		let errorMsg = error.message;
		let code = error.code;
	} );
}

function testForResults(acronym){
	const filter1 = wixData.filter()
	.contains("acronym", acronym)

	wixData.aggregate("OrganizationEntries")
	.filter(filter1)
	.run()
	.then( (results) => {
		console.log(results.items.length)
		if (results.items.length == 0) {
            //If we have no items, display the no results pane
			$w('#box21').expand();
		}
	} )
	.catch( (error) => {
		let errorMsg = error.message;
		let code = error.code;
	} );
}