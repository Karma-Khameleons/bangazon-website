console.log("hi");
$('#cat-list').on('change', function() {
	console.log("this.value", this.value);
	// console.log("this.value", this.value);
	// console.log("this.value", this.value);
	if (this.value == 'new')
		$('#newCat').removeClass('hidden');
		$('#cat-list').addClass('hidden');
		$('#cats').addClass('hidden');
	if (this.value != 'new')
		$('#product_type_id').text(this.value);
		console.log("id", this.value);
		$('#oldCat').removeClass('hidden');
		$('#cat-list').addClass('hidden');
		$('#cats').addClass('hidden');
});