<script>
  import { Body, Button, Heading, Icon, Input, Layout } from "@budibase/bbui"
  import {
    readableToRuntimeBinding,
    runtimeToReadableBinding,
  } from "builderStore/dataBinding"
  import DrawerBindableInput from "components/common/bindings/DrawerBindableInput.svelte"

  export let bindable = true
  export let queryBindings = []
  export let bindings = []
  export let customParams = {}

  function newQueryBinding() {
    queryBindings = [...queryBindings, {}]
  }

  $: console.log(bindings)

  function deleteQueryBinding(idx) {
    queryBindings.splice(idx, 1)
    queryBindings = queryBindings
  }

  // This is necessary due to the way readable and writable bindings are stored.
  // The readable binding in the UI gets converted to a UUID value that the client understands
  // for parsing, then converted back so we can display it the readable form in the UI
  function onBindingChange(param, valueToParse) {
    customParams[param] = readableToRuntimeBinding(bindings, valueToParse)
  }
</script>

<Layout noPadding={bindable} gap="S">
  <div class="controls" class:height={!bindable}>
    <Heading size="XS">Bindings</Heading>
    {#if !bindable}
      <Button secondary on:click={newQueryBinding}>Add Binding</Button>
    {/if}
  </div>
  <Body size="S">
    {#if !bindable}
      Bindings come in two parts: the binding name, and a default/fallback
      value. These bindings can be used as Handlebars expressions throughout the
      query.
    {:else}
      Enter a value for each binding. The default values will be used for any
      values left blank.
    {/if}
  </Body>
  <div class="bindings" class:bindable>
    {#each queryBindings as binding, idx}
      <Input
        placeholder="Binding Name"
        thin
        disabled={bindable}
        bind:value={binding.name}
      />
      <Input
        placeholder="Default"
        thin
        disabled={bindable}
        bind:value={binding.default}
      />
      {#if bindable}
        <DrawerBindableInput
          title={`Query binding "${binding.name}"`}
          placeholder="Value"
          thin
          on:change={evt => onBindingChange(binding.name, evt.detail)}
          value={runtimeToReadableBinding(
            bindings,
            customParams?.[binding.name]
          )}
          {bindings}
        />
      {:else}
        <Icon hoverable name="Close" on:click={() => deleteQueryBinding(idx)} />
      {/if}
    {/each}
  </div>
</Layout>

<style>
  .bindings.bindable {
    grid-template-columns: 1fr 1fr 1fr;
  }

  .controls {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .bindings {
    display: grid;
    grid-template-columns: 1fr 1fr 5%;
    grid-gap: 10px;
    align-items: center;
  }

  .height {
    height: 40px;
  }
</style>
