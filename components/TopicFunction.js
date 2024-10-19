export function TopicFunction({ channels }) {
    const topicsDetails = getTopics(channels)
    let functions = ''
  
    topicsDetails.forEach((t) => {
      functions += `def send${t.name}(self, id, location, extra):
          topic = "${t.topic}"
          message = {
            "alertId": id,
            "location": location,
            ${t.extraField ? `"${t.extraField}": extra,` : ''}
          }
          result = self.client.publish(topic, json.dumps(message))
          rc, mid = result
          if rc == mqtt.MQTT_ERR_SUCCESS:
              print(f"${t.name} Message with id {mid} published successfully.")
          else:
              print(f"Failed to publish message with id {mid}. Error code: {rc}")
          \n`

    })
  
    return functions
  }
  
  function getTopics(channels) {
    const channelsCanSendTo = channels
    let topicsDetails = []
  
    channelsCanSendTo.forEach((ch) => {
      const topic = {}
      const operationId = ch.operations().filterByReceive()[0].id()
      topic.name = operationId.charAt(0).toUpperCase() + operationId.slice(1)
      topic.topic = ch.address()

      if (operationId === 'rainAlert' || operationId === 'snowAlert') {
        topic.extraField = 'intensity'
      } else if (operationId === 'heatwaveAlert' || operationId === 'normalAlert') {
        topic.extraField = 'temperature'
      }
  
      topicsDetails.push(topic)
    })
  
    return topicsDetails
  }
