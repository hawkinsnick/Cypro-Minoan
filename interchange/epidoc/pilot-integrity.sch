<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://purl.oclc.org/dsdl/schematron"
        xmlns:tei="http://www.tei-c.org/ns/1.0"
        queryBinding="xslt2">
  <title>Cypro-Minoan partial occurrence pilot integrity profile</title>
  <ns prefix="tei" uri="http://www.tei-c.org/ns/1.0"/>
  <pattern id="partial-coverage">
    <rule context="tei:div[@type='edition']">
      <assert test="@subtype='partial-source-assertions'">Pilot edition must declare partial source assertions.</assert>
      <assert test="tei:ab[contains(concat(' ', normalize-space(@ana), ' '), ' #partial-coverage ')]">Pilot edition must explicitly mark partial coverage.</assert>
    </rule>
  </pattern>
  <pattern id="sign-evidence">
    <rule context="tei:g">
      <assert test="@xml:id">Each sign occurrence must have an XML identifier.</assert>
      <assert test="starts-with(@ref, 'urn:cypro-minoan:published-sign:')">Each sign must retain a source-qualified sign reference.</assert>
      <assert test="starts-with(@resp, '#source-')">Each sign must retain its source authority.</assert>
      <assert test="ancestor::tei:div[@type='edition']">Sign occurrences must be in a declared edition.</assert>
      <assert test="//tei:note[@type='source-locator'][@corresp=concat('#', current()/@xml:id)]">Each sign must have a source locator.</assert>
    </rule>
  </pattern>
</schema>
