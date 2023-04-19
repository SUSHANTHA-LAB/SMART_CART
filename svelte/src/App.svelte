<script>
	
    import items from './data.json';
	
	let itemsList = items;
	let total = 0;

	for(let i = 0; i < itemsList.length; i++) {
    	let obj = itemsList[i];
		total = total + obj.price;
	}

	function removeFromList(index) {
		total = total - itemsList[index].price
		itemsList.splice(index, 1)
		itemsList = itemsList;

    }
</script>

<main>
	<div class="container-sm heading">
		<h4 class="d-flex justify-content-between align-items-center mb-3">
            <span class="text-primary">Your Cart    
				
			</span>
			<button class="btn btn-outline-success" type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
				Product Info
			</button>
            <span class="badge bg-primary rounded-pill">
				
				{itemsList.length}</span>
        </h4>
		
	{#each itemsList as item, index}
	<ol class="list-group itemslist">
		<li class="list-group-item d-flex justify-content-between align-items-start">
		  <div class="ms-2 me-auto">
			<div class="fw-bold">{index+1}. {item.display_name}</div>

			  <div class="collapse" id="collapseExample">
				<div class="card card-body">
					<h6 class="card-subtitle mb-2 text-body-secondary">Manufacturer: {item.manufacturer}</h6>
					<h6 class="card-subtitle mb-2 text-body-secondary">Net Weight: {item.weight}</h6>
					<p class="card-text">Nutritional Facts:<br>{item.nutri_facts}</p>

				</div>
			  </div>
		  </div>
		  <span class="price">{item.price} &#8377;</span>
		  <button on:click={() => removeFromList(index)} class="btn btn-outline-danger btn-close"></button>
		</li>
	</ol>
	{/each} 

	<ol class="list-group total">
		<li class="list-group-item d-flex justify-content-between align-items-start">
		  <div class="ms-2 me-auto">
			<div class="fw-bold">
				<h5>Total</h5> 
			</div>
	   
		  </div>
		  <strong >{total} &#8377;</strong>
		  <!--<span class="badge bg-primary rounded-pill">14</span>
		  -->
		</li>
	  </ol>

	  <div class="d-grid gap-2 d-md-flex justify-content-md-end pay">
		<button class="btn btn-outline-success" type="button" >Pay and Checkout</button>
		
	  </div>

</div>
</main>
<style>
	.heading{
    padding-top: 20px;
    padding-bottom: 20px;
}

.itemslist{
    padding-bottom: 10px;
}

.total{
    padding-bottom: 20px;

}

.pay{
    padding: 0px;
}

.price{
	padding-top: 8px;
	padding-right: 5px;
}

</style>