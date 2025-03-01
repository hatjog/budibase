<script>
  import { get } from "svelte/store"
  import { getContext, onDestroy } from "svelte"
  import { ModalContent, Modal } from "@budibase/bbui"
  import FilterModal from "./FilterModal.svelte"
  import { buildLuceneQuery } from "builder/src/helpers/lucene"
  import Button from "../Button.svelte"

  export let dataProvider
  export let allowedFields
  export let size = "M"

  const component = getContext("component")
  const { builderStore, ActionTypes, getAction, fetchDatasourceSchema } =
    getContext("sdk")

  let modal
  let tmpFilters = []
  let filters = []
  let schemaLoaded = false,
    schema

  $: dataProviderId = dataProvider?.id
  $: addExtension = getAction(
    dataProviderId,
    ActionTypes.AddDataProviderQueryExtension
  )
  $: removeExtension = getAction(
    dataProviderId,
    ActionTypes.RemoveDataProviderQueryExtension
  )
  $: fetchSchema(dataProvider || {})
  $: schemaFields = getSchemaFields(schema, allowedFields)

  // Add query extension to data provider
  $: {
    if (filters?.length) {
      const queryExtension = buildLuceneQuery(filters)
      addExtension?.($component.id, queryExtension)
    } else {
      removeExtension?.($component.id)
    }
  }

  async function fetchSchema(dataProvider) {
    const datasource = dataProvider?.datasource
    if (datasource) {
      schema = await fetchDatasourceSchema(datasource, {
        enrichRelationships: true,
      })
    }
    schemaLoaded = true
  }

  function getSchemaFields(schema, allowedFields) {
    if (!schemaLoaded) {
      return {}
    }
    let clonedSchema = {}
    if (!allowedFields?.length) {
      clonedSchema = schema
    } else {
      allowedFields?.forEach(field => {
        clonedSchema[field] = schema[field]
      })
    }
    return Object.values(clonedSchema || {})
  }

  const openEditor = () => {
    if (get(builderStore).inBuilder) {
      return
    }
    tmpFilters = [...filters]
    modal.show()
  }

  const updateQuery = () => {
    filters = [...tmpFilters]
  }

  onDestroy(() => {
    removeExtension?.($component.id)
  })
</script>

{#if schemaLoaded}
  <Button
    onClick={openEditor}
    icon="Properties"
    text="Filter"
    {size}
    type="secondary"
    quiet
    active={filters?.length > 0}
  />

  <Modal bind:this={modal}>
    <ModalContent title="Edit filters" size="XL" onConfirm={updateQuery}>
      <FilterModal bind:filters={tmpFilters} {schemaFields} />
    </ModalContent>
  </Modal>
{/if}
